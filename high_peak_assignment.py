#!/usr/bin/env python
# coding: utf-8

# In[4]:


def calculate(st,et,ear):
    detail = list(zip(st,et,ear))
    maxear = sorted(ear)
    detail.sort(key=lambda a:a[0])
    sal = maxear[-1]
    jobs = 1
    for i,j,k in detail[:-1]:
        sal2 = k
        c = 1
        for l,m,n in detail[1:]:
            if l>j:
                sal2 += n
                j = m 
                c += 1
        if sal2 > sal:
            sal = sal2
            jobs = c
    # print('-'*50)
    # print(f'Lokesh did {jobs} jobs today and earned {sal}')
    # print('-'*50)
    print(f'Number of jobs remaining {len(st)-jobs}')
    print(f'Earnings of other employees: {sum(ear)-sal}')
        



n = int(input('Enter number of jobs: '))
st = []
et = []
ear = []
for i in range(1,n+1):
    st.append(int(input(f'Enter starting time {i} job: ')))
    et.append(int(input(f'Enter ending time {i} job: ')))
    ear.append(int(input(f'Enter earning of {i} job: ')))
calculate(st,et,ear)
