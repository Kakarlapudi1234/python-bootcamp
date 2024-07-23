# print the element in a particular index, the codition is cyclic printing. (find the element prresent in kth inddex)
#k=20
#70 54 36 72 76 9999 0089    k=20,7
# 1  2  3  4  5   6    7       ix=6
#===============================================================================================
# k=18
# 80 70 54 36 77              k=18,5
#  1  2  3  4  5              idx=3
# ===============================================================================================
# k=38
# 70 54 36 72 566             k=38,5
#  1  2  3  4  5              idx=3 ******Imp   
my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])
