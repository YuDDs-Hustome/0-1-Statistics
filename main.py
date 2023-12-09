import matplotlib.pyplot as plt 
import necessary_define as nd
import numpy as np
import pandas as pd

s = 1 # Đặt kèo Xỉu = 0, Tài = 1. Thua = -1!
m = 4 # Số tiền đặt ban đầu
ng = 3 # Số lần gấp thếp quy định
dead_point = 0 
for i in range(0, ng):
    dead_point += m*(2**i) # Ngưỡng thất bại
# print(dead_point)
    
an = 0
thua = 0
hoa = 0
solankhaosat = 10000
v_agv = []
v_agv_an = []
v_agv_thua = []
c_thua = []
c_thang = []

for i in range(0, solankhaosat): # Số phép thử

    ##############################################################################################################################
    v = 100 # Vốn ban đầu
    target = 2 # Rate 
    v_const = v
    v_status = []
    n = 100 # Số lần chơi
    c = 0 # Biến đếm số lần chơi
    g = 0 # Biến trạng thái gấp thếp [m*(2**g)] - lựa chọn gấp đôi

    # if n > 0:   
    #     print(f"{c}: {v} -> Cược {m*(2**g)} cho lần tiếp")
    while(v >= dead_point and v <= v_const*target):
        v -= m*(2**g)
        result = nd.dice()
        if result == s: 
            v += 2*m*(2**g)
            g = 0
        else:
            # Thua sẽ gấp thếp đến số lần quy định (ng). Nếu đến số lần quy định không ăn thì ngừng gấp thếp và chơi lại từ đầu.
            g += 1 
            if g >= ng:
                g = 0
        v_status.append(v) # Thu thập khảo sát trạng thái vốn

        c += 1
        # if c > n: # Cài đặt số lần chơi 
        #     break
    #     else:
    #         if g > 0:
    #             print(f"{c}*: {v} -> Cược {m*(2**g)} cho lần tiếp") # Ký hiệu * đánh dấu lần chơi bị thua!
    #         else:
    #             print(f"{c}: {v} -> Cược {m*(2**g)} cho lần tiếp")

    # # Kết luận trên một lần khảo sát    
    # print(f"Sau {c} lần, số tiền thu được là {v}")
        
    # # Vẽ giao động vốn
    # if n > 1:
    #     plt.plot(range(0, len(v_status)), v_status, label='Đường giao động vốn')
    #     plt.axhline(y=v_const, color='g', linestyle='--', label='Đường vốn ban đầu')
    #     plt.axhline(y=v_const*target, color='b', linestyle='--', label='Đường mục tiêu')
    #     plt.axhline(y=dead_point, color='r', linestyle='--', label='Đường chết')

    #     # Các thông số tùy chỉnh hiển thị
    #     plt.title('Đồ thị khảo sát giá trị vốn khi chơi Sicbo')
    #     plt.xlabel('Số lần chơi')
    #     plt.ylabel('Giá trị vốn còn lại (VND)')
    #     plt.legend()
    #     plt.xticks(range(0, c + 10, 10))  
    #     plt.yticks(range(-int(2*v_const*0.05), int(2*v_const + 2*v_const*0.1), int(2*v_const*0.05)))
    #     plt.grid(True)
    #     plt.show()
    #############################################################################################################################
    v_agv.append(v_status)
    if v >= 128:
        an += 1
        v_agv_an.append(v_status)
        c_thang.append(c)
    elif v <= 72:
        thua += 1
        v_agv_thua.append(v_status)
        c_thua.append(c)
    else:
        hoa += 1

# Kết luận trên nhiều lần khảo sát    
# print(f"Ty le An: {an/(solankhaosat/100)}")
# print(f"Ty le Thua: {thua/(solankhaosat/100)}")
# print(f"Ty le Hoa: {hoa/(solankhaosat/100)}")
print(f"Trung bình đến {np.mean(c_thang)} lần sẽ thắng đủ Target") 
print(f"Trung bình đến {np.mean(c_thua)} lần sẽ thua hết")

#############################################################################################################################
df = pd.DataFrame(v_agv)
df = df.apply(lambda x: pd.Series(x).fillna(pd.NaT))
mean_column = (df.mean()).tolist()
plt.figure(1)
plt.plot(range(0, len(mean_column)), mean_column, label='Đường giao động vốn')
plt.axhline(y=v_const, color='g', linestyle='--', label='Đường vốn ban đầu')
plt.axhline(y=v_const*target, color='b', linestyle='--', label='Đường mục tiêu')
plt.axhline(y=dead_point, color='r', linestyle='--', label='Đường chết')

plt.title('Đồ thị khảo sát giá trị trung bình vốn khi chơi Sicbo')
plt.xlabel('Số lần chơi')
plt.ylabel('Giá trị vốn còn lại (VND)')
plt.legend()
plt.xticks(range(0, len(mean_column) + 10, int(len(mean_column)*0.1)))  
plt.yticks(range(-int(2*v_const*0.05), int(2*v_const + 2*v_const*0.1), int(2*v_const*0.05)))
plt.grid(True)

#############################################################################################################################
df = pd.DataFrame(v_agv_an)
df = df.apply(lambda x: pd.Series(x).fillna(pd.NaT))
mean_column = (df.mean()).tolist()
plt.figure(2)
plt.plot(range(0, len(mean_column)), mean_column, label='Đường giao động vốn')
plt.axhline(y=v_const, color='g', linestyle='--', label='Đường vốn ban đầu')
plt.axhline(y=v_const*target, color='b', linestyle='--', label='Đường mục tiêu')
plt.axhline(y=dead_point, color='r', linestyle='--', label='Đường chết')

plt.title('Đồ thị khảo sát giá trị thắng vốn khi chơi Sicbo')
plt.xlabel('Số lần chơi')
plt.ylabel('Giá trị vốn còn lại (VND)')
plt.legend()
plt.xticks(range(0, len(mean_column) + 10, int(len(mean_column)*0.1)))  
plt.yticks(range(-int(2*v_const*0.05), int(2*v_const + 2*v_const*0.1), int(2*v_const*0.05)))
plt.grid(True)

#############################################################################################################################
df = pd.DataFrame(v_agv_thua)
df = df.apply(lambda x: pd.Series(x).fillna(pd.NaT))
mean_column = (df.mean()).tolist()
plt.figure(3)
plt.plot(range(0, len(mean_column)), mean_column, label='Đường giao động vốn')
plt.axhline(y=v_const, color='g', linestyle='--', label='Đường vốn ban đầu')
plt.axhline(y=v_const*target, color='b', linestyle='--', label='Đường mục tiêu')
plt.axhline(y=dead_point, color='r', linestyle='--', label='Đường chết')

plt.title('Đồ thị khảo sát giá trị thua vốn khi chơi Sicbo')
plt.xlabel('Số lần chơi')
plt.ylabel('Giá trị vốn còn lại (VND)')
plt.legend()
plt.xticks(range(0, len(mean_column) + 10, int(len(mean_column)*0.1)))  
plt.yticks(range(-int(2*v_const*0.05), int(2*v_const + 2*v_const*0.1), int(2*v_const*0.05)))
plt.grid(True)

#############################################################################################################################
plt.figure(4)
categories = ['Ăn', 'Thua', 'Hòa']
values = [an/(solankhaosat/100), thua/(solankhaosat/100), hoa/(solankhaosat/100)]
plt.bar(categories, values)

plt.xlabel('Trạng thái')
plt.ylabel('Tỷ lệ (%)')
plt.title(f"Đồ thị khảo sát trạng thái trên {solankhaosat} lần")

#############################################################################################################################
plt.show()
