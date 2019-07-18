clear

project_root = getenv('XL_ROOT');
if isempty(project_root)
    project_root = '/Users/eshed/projects/xl-vertices';
end

files = dir(fullfile(project_root, 'processed_data', '*.mat'));
allData = cell(13248,7);
iData = 1;
for iFiles= 1:length(files)
    file = files(iFiles);
    load([file.folder '/' file.name], 'log');
    
    splitLoc = strfind(file.name,'_');
    xlsFile = dir([file.folder '/' file.name(1:(splitLoc(end)-1)) '*.xls']);
    if contains(xlsFile.name, 'Forward')
        posOrder = 1:5;
    elseif contains(xlsFile.name, 'Backward')
        posOrder = 5:-1:1;
    else
        error('unexpected filename');
    end
    [scoredResponse,~,~] = xlsread([xlsFile.folder '/' xlsFile.name]);
    
    for iTrial = 1:length(log)
        allData(iData,1) = log(iTrial,1);
        allData{iData,5} = [num2str(iFiles) file.name(1:2)];
        splitLoc = strfind(log{iTrial,2},'_');
        baseName = log{iTrial,2}(1:(splitLoc(end)-1));
        allData{iData,2} = baseName;
        allData(iData,3) = log(iTrial,3);
        allData{iData,4} = posOrder(log{iTrial,4});
        
        allData{iData,7} = scoredResponse(iTrial);
        
        if endsWith(log{iTrial,2}, 'o.jpg')
            allData{iData,6} = 'o';
        elseif endsWith(log{iTrial,2}, 'ox.jpg')
            allData{iData,6} = 'ox';
        elseif endsWith(log{iTrial,2}, 'cd.jpg')
            allData{iData,6} = 'cd';
        elseif endsWith(log{iTrial,2}, 'cdx.jpg')
            allData{iData,6} = 'cdx';
        elseif endsWith(log{iTrial,2}, 'cdl.jpg')
            allData{iData,6} = 'cdl';
        else
            error('unexpected stimulus name');
        end
        iData = iData + 1;
    end
end

dataTable = cell2table(allData, 'VariableNames', {'TrialNum', 'Stimulus', 'RT', 'Repetition', 'SubjectID', 'Condition', 'ScoredResponse'});
out_file = fullfile(project_root, 'processed_data', 'alldata.csv');
writetable(dataTable, out_file);
