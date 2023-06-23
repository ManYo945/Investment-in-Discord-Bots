import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import datetime

def normalized_data(data):
    min_value = np.min(data)
    max_value = np.max(data)    
    normalized = (data - min_value) / (max_value - min_value)  
    return normalized

def get_N225_temp(flag):
    N225 = yf.Ticker("^N225").history(start=start_date, end=end_date)
    N225_close_n = normalized_data(N225.Close)
    if flag == 1:
        plt.plot(N225_close_n)
        np.shape(N225_close_n)
    return N225_close_n

def get_JYTWD_temp(flag):
    JPYTWD = yf.Ticker("JPYTWD=X").history(start=start_date, end=end_date)
    JPYTWD_close_n = normalized_data(JPYTWD.Close)
    if flag == 1:
        plt.plot(JPYTWD_close_n)
        np.shape(JPYTWD_close_n)
    return JPYTWD_close_n


start_date = (datetime.datetime.now() - datetime.timedelta(days=20)).strftime('%Y-%m-%d')
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

N225_close_n = get_N225_temp(0)
JPYTWD_close_n= get_JYTWD_temp(0)

correlation = np.corrcoef(N225_close_n, JPYTWD_close_n)[0, 1]

plt.plot(N225_close_n, color="red", label='N225_close')
plt.plot(JPYTWD_close_n, color="blue",label='JPYTWD_close')
x_label = JPYTWD_close_n.index
plt.title("correlation: "+ str(correlation))
plt.xticks([x_label[0], x_label[-1]])
plt.legend()

if correlation > 0:
    print("x 和 y 呈正相關")
elif correlation < 0:
    print("x 和 y 呈負相關")
else:
    print("x 和 y 無相關性")

plt.savefig('N225&JPYTWD.png')
