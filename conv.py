# -*- coding:utf-8 -*-
import sys, csv

def load_config_csv(fname):
    try:
        with open(fname, 'rt', encoding='utf-8', newline=None) as f:
            cin = csv.DictReader(f)
            cfg = dict()
            header = list()
            for row in cin:
                # (行番号, 列番号)をキーにする
                k = (int(row['row']), int(row['column']),)
                cfg[k] = row['name']
                header.append(row['name'])

            return (cfg, header)
    except Exception as e:
        raise e

def main():
    _, cfgf, dataf = sys.argv

    cfg, header = load_config_csv(cfgf)
    
    try:
        with open(dataf, 'rt', encoding='utf-8', newline=None) as f:
            cin = csv.reader(f)
            d = dict()
            for nrow, row in enumerate(cin, 1):
                for ncolumn, value in enumerate(row, 1):
                    k = (nrow, ncolumn)
                    if k in cfg:
                        d[cfg[k]] = value

            cout = csv.writer(sys.stdout)
            cout.writerow(header)
            cout.writerow([d[name] for name in header if name in d])
            
    except Exception as e:
        raise e

if __name__=='__main__':
    main()
