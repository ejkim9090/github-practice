from decimal import Decimal

print(0.1+0.2) 
# 0.30000000000000004

print( Decimal(1) / Decimal(10) + Decimal(2) / Decimal(10))
# 0.3

print( Decimal('0.1') + Decimal('0.2'))
# 0.3

# Decimal 실수 작성시 ' ' 필요함!
print( Decimal(0.1))   # 0.1000000000000000055511151231257827021181583404541015625
print( Decimal('0.1'))  # 0.1

