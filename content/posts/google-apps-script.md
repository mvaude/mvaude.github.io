+++
draft = true
date = 2018-06-06
title = "Google Apps Script"
slug = "Google Apps Script"
tags = ["scripting", "javascript", "cloud", "web"]
categories = ["scripting", "javascript", "cloud", "web"]
+++

## Google Spreadsheet

### Add a Custom menu

It will let us call our functions from the spreadsheet.

```
function onOpen(e) {
  var menu = SpreadsheetApp.getUi().createMenu('Resources')

  menu.addItem('Send Report', 'sendReport')
  .addSeparator()
  .addSubMenu(SpreadsheetApp.getUi().createMenu('Data')
  .addItem('Update', 'updateData')
  .addItem('Remove Source', 'removeDataSource'))
  .addToUi();
}
```
