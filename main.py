import pandas as panda


# Get CSV Data
data = panda.read_csv (r'C:\Users\JS6845\Downloads\batt_log_1.csv')

# Columns List
headers = ['Date/Time', 'Battery Remaining', 'Battery Current', 'Battery Status']

# InitData Frame & Dictionary
splitCsvDictionary = {}
csvDataFrame = panda.DataFrame(data, columns=headers)

# Holder for previous value & cut index
numberOfDischargeBlocks = 0
startIndexOfDischargeBlock = 0
startIndexSet = False
previousBatteryStatus = csvDataFrame.iloc[0]['Battery Status']

# Loop all rows in file
for index, row in csvDataFrame.iterrows():
    # Get current status
    currentStatus = csvDataFrame.iloc[index]['Battery Status']

    # Update start index of discharging block, if applicable
    if startIndexSet is False and currentStatus == 'Discharging':
        startIndexOfDischargeBlock = index
        startIndexSet = True

    # Cut the data at this point - we've looped through a discharging block,
    # and then hit a block which is anything other than discharging.
    # we need to take the data from the last cut point up to the current point,
    # and put that into its own ArrayList (or dictionary)
    if previousBatteryStatus == 'Discharging' and currentStatus != 'Discharging':
        splitCsvDictionary[numberOfDischargeBlocks] = csvDataFrame[startIndexOfDischargeBlock:index]
        numberOfDischargeBlocks = numberOfDischargeBlocks + 1
        startIndexSet = False

    # UpdateHolder
    previousBatteryStatus = currentStatus

# We've created a dictionary with a dataframe for each discharging block, so lets loop the data frames and save each one
# as an xlsx file
for key, dataFrame in splitCsvDictionary.items():
    dataFrame.to_excel(r'C:\Users\JS6845\\Downloads\batt_log_1_{}.xlsx'.format(key), index=False, header=True)

# ======================================================================================================================

# data = pd.read_csv (r'C:\Users\JS6845\Downloads\batt_log_1.csv')
# df = pd.DataFrame(data, columns=['Date/Time', 'Battery Remaining', 'Battery Current', 'Battery Status'])
#
# previousRow = ""
# dischargingChunks = {}
# numberOfIterations = 0
# startIndex = 0
# for currentIndex, row in df.iterrows():
#     currentItem = row['Battery Status']
#     nextItem = df['Battery Status'][row+1]
#     if currentItem=='Discharging' and nextItem=='Charging':
#         dischargingChunks[numberOfIterations] = df[startIndex:currentIndex]
#         startIndex = currentIndex
#         numberOfIterations = numberOfIterations + 1
#
#     previousRow = row['Battery Status']
#
# for dateTimeKey in dischargingChunks.keys():
#     print(dischargingChunks[dateTimeKey])

# ======================================================================================================================
