import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race').size().sort_values(ascending=False) #OK

    # average age of men
    average_age_men = df[df['sex']=='Male']['age'].mean().round(1)#ok

    # percentage, Bachelor's degree
    TotalNumber=df['education'].size #用之前要做data cleaning,如有missing data, total會錯
    Series_edu = df.groupby('education').size() #value is number
    percentage_bachelors = (Series_edu['Bachelors']/TotalNumber*100).round(1)#ok

    # percentage, advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K
    AdvancedEdu = df[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')] #df
    
    AdvancedEdu_totalnum=AdvancedEdu['education'].size #7491
    AdvancedEdu_more50k= AdvancedEdu[AdvancedEdu['salary']=='>50K']['salary'].size #3486
  
    # percentage, lower education
    LowerEdu = df[(df['education']!='Bachelors')&(df['education']!='Masters')&(df['education']!='Doctorate')]
    LowerEdu_totalnum=LowerEdu['education'].size #25070
    LowerEdu_more50k=LowerEdu[LowerEdu['salary']=='>50K']['salary'].size #4355
  
    # percentage with salary >50K
    higher_education_rich = round(AdvancedEdu_more50k/AdvancedEdu_totalnum*100,1)#ok
    lower_education_rich = round(LowerEdu_more50k/LowerEdu_totalnum*100,1) #ok

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min() #1
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
      #有幾多人係做min work hours
    df_num_min_workers = df[df['hours-per-week']==min_work_hours]
    num_min_workers =df_num_min_workers['hours-per-week'].size #20
      #有幾多人係做min work hours,仲>50k
    df_num_min_workers_more50k=df_num_min_workers[df_num_min_workers['salary']=='>50K']
    num_min_workers_more50k=df_num_min_workers_more50k['salary'].size#2
      #percentage
    rich_percentage=num_min_workers_more50k/num_min_workers*100 #ok

    # What country has the highest percentage of people that earn >50K?
    a=df[df['salary']=='>50K'].groupby('native-country').size() #distribution_country,df,>50K
    C_text=''
    highest_value=0
    for i in a.index:
      C_result=a[i]/df[df['native-country']==i]['native-country'].size
      if C_result>highest_value:
        highest_value=C_result
        C_text=i
    highest_earning_country=C_text #ok
    highest_earning_country_percentage = round((a[C_text]/df[df['native-country']==C_text]['native-country'].size)*100,1)
    # Identify the most popular occupation for those who earn >50K in India.

    top_IN_occupation = df[(df['native-country']=='India')&(df['salary']=='>50K')].groupby('occupation').size().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
