"""
Purpose:
    This script identifies the subjects for whom we have both RT and Error Rate data, and 
    puts those logs in a new folder called valid_logs

Author:
    Eshed Margalit
    eshed.margalit@gmail.com
"""

import glob
import os
import shutil

def get_log_ids(project_root):
    """
    Strips prefixes and suffixes to match rt and audio logs
    """
    rt_log_path = os.path.join(project_root, 'raw_data', 'rt_logs')
    audio_log_path = os.path.join(project_root, 'raw_data', 'scored_audio_logs')

    rt_logs = glob.glob(os.path.join(rt_log_path, '*.mat'))
    audio_logs = glob.glob(os.path.join(audio_log_path, '*.xls'))

    # Strip prefixes and suffixes
    rt_log_ids = [x.split('/')[-1].split('_Data.mat')[0] for x in rt_logs]
    audio_log_ids = ['_'.join(x.split('/')[-1].split('_')[0:2]) for x in audio_logs]

    return rt_log_ids, audio_log_ids

def copy_valid_logs(log_overlap, project_root):
    write_dir = os.path.join(project_root, 'processed_data')
    rt_log_path = os.path.join(project_root, 'raw_data', 'rt_logs')
    audio_log_path = os.path.join(project_root, 'raw_data', 'scored_audio_logs')

    if not os.path.isdir(write_dir):
        os.makedirs(write_dir)

    list_types = []
    for log_id in log_overlap:
        rt_log_pattern = os.path.join(rt_log_path, '%s*.mat' % log_id)
        matching_rt_log = glob.glob(rt_log_pattern)[0]
        matching_rt_log_path = os.path.sep.join(matching_rt_log.split(os.path.sep)[-1:])
        shutil.copy(matching_rt_log, os.path.join('processed_data', matching_rt_log_path))

        audio_log_pattern = os.path.join(audio_log_path, '%s*.xls' % log_id)
        matching_audio_log = glob.glob(audio_log_pattern)[0]
        matching_audio_log_path = ''.join(matching_audio_log.split(os.path.sep)[-1:])
        shutil.copy(matching_audio_log, os.path.join('processed_data', matching_audio_log_path))

        list_type = '_'.join(matching_audio_log_path.split('.xls')[0].split('_')[2:4])
        list_types.append(list_type)

def main():
    project_root = os.environ.get('XL_ROOT', '/Users/eshed/projects/xl-vertices')
    rt_log_ids, audio_log_ids = get_log_ids(project_root)
    log_overlap = list(set(rt_log_ids) & set(audio_log_ids))

    copy_valid_logs(log_overlap, project_root)


if __name__ == "__main__":
    main()
