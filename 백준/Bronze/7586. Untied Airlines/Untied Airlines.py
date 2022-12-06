check = {'L': 120, 'S': 150, 'B': 150, 'N': 40,
         'C': 160, 'D': 100, 'R': 100, 'O': 100}
while (airline:=input()) != '#':
    rec = {}
    while (poor_service:=input()) != '00A':
        seat, poor_service_code = poor_service.split()
        try:
            rec[seat] += check[poor_service_code]
        except:
            if poor_service_code in 'LSBNCDRO':
                rec[seat] = check[poor_service_code]
    print(airline, sum(i >= 200 for i in rec.values()))