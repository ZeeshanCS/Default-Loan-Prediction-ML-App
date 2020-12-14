import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'loan_amnt':5000, 'funded_amnt':5000, 'funded_amnt_inv':4975,
                            'term':0, 'int_rate':78, 'installment':162, 'grade':1, 
                            'sub_grade':6, 'emp_title':24614, 'emp_length':1, 
                            'home_ownership':4, 'annual_inc':24000, 'verification_status':2,
                            'issue_d':13, 'desc':20677, 'purpose':1, 'title':3158, 
                            'zip_code':726, 'addr_state':3, 'dti':27, 'delinq_2yrs':0,
                            'earliest_cr_line':192, 'inq_last_6mths':1, 'open_acc':3,
                            'pub_rec':3, 'revol_bal':13648, 'revol_util':942, 'total_acc':9,
                            'total_pymnt':5863, 'total_pymnt_inv':5833, 'total_rec_prncp':5000,
                            'total_rec_int':863, 'total_rec_late_fee':0, 'recoveries':0,
                            'collection_recovery_fee':0, 'last_pymnt_d':46, 
                            'last_pymnt_amnt':171, 'last_credit_pull_d':21, 'acc_now_delinq':0,
                            })

print(r.json())