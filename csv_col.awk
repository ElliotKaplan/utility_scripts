#!/usr/bin/awk -f

BEGIN {
    if (ARGC == 0) {
        print("csv_col.awk [-v sep=\",\"] [-v row=1] [-v reg=<regex>] targetfile");
        print("Reads the specified row of a file (default first) and print an itemized list of column names");
        print("Default separator is \",\"");
        print("Set \"reg\" to use regular expression to find column header line")
    };
    # default to commas
    if (sep=="") sep = ",";
    FS = sep;
    # default to first row
    if (row == "") row = 1;
    if (reg == "") usereg=0;  else {
        usereg=1;
        row=-1;
    };
}
((usereg && ($0 ~ reg)) || (NR == row)){
    for (i=1; i<=NF; i++) {
        print(i "\011" $i);
    };
    exit;
};
    
