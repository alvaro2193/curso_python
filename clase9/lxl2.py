with open ('myfile.txt', 'r') as fp :
    while True :
        curl_line = fp.readline ()

        if curl_line == '':
        break
        print (curl_line)