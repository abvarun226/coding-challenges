def campusCup(emails):
    domains = {}
    for email in emails:
        name, domain = email.split('@')
        if domain not in domains:
            domains[domain] = 0
        domains[domain] += 20
    for domain, val in domains.items():
        if val < 100:
            domains[domain] = 0
        elif val < 200:
            domains[domain] = 3
        elif val < 300:
            domains[domain] = 8
        elif val >= 300 and val < 500:
            domains[domain] = 15
        else:
            domains[domain] = 25

    dlist = list(domains.keys())
    for i in range(len(dlist)):
        for j in range(i, len(dlist)):
            if domains[dlist[i]] < domains[dlist[j]]:
                dlist[i], dlist[j] = dlist[j], dlist[i]
            elif domains[dlist[i]] == domains[dlist[j]] and dlist[i] > dlist[j]:
                dlist[i], dlist[j] = dlist[j], dlist[i]
    return dlist

emails = ["b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru", 
 "f@rain.ifmo.ru", 
 "g@rain.ifmo.ru", 
 "h@rain.ifmo.ru", 
 "i@rain.ifmo.ru", 
 "j@rain.ifmo.ru", 
 "k@rain.ifmo.ru", 
 "l@rain.ifmo.ru", 
 "m@rain.ifmo.ru", 
 "n@rain.ifmo.ru", 
 "o@rain.ifmo.ru", 
 "p@rain.ifmo.ru", 
 "q@rain.ifmo.ru", 
 "r@rain.ifmo.ru", 
 "s@rain.ifmo.ru", 
 "t@rain.ifmo.ru", 
 "u@rain.ifmo.ru", 
 "v@rain.ifmo.ru", 
 "w@rain.ifmo.ru", 
 "x@rain.ifmo.ru", 
 "y@rain.ifmo.ru", 
 "a@mit.edu.ru", 
 "b@mit.edu.ru", 
 "c@mit.edu.ru", 
 "d@mit.edu.ru", 
 "e@mit.edu.ru", 
 "f@mit.edu.ru", 
 "g@mit.edu.ru", 
 "h@mit.edu.ru", 
 "i@mit.edu.ru", 
 "j@mit.edu.ru", 
 "k@mit.edu.ru", 
 "l@mit.edu.ru", 
 "m@mit.edu.ru", 
 "n@mit.edu.ru", 
 "o@mit.edu.ru"]

print(campusCup(emails))

