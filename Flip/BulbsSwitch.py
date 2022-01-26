"""
find min times to switch bulbs to make all bulbs on
1 means a bulb is on, 0 means off
"""

def miniFlipstoSetAllElements(arr):
  count=0
  while True:
    if 0 not in arr:
      break
    count+=1
    start=-1
    i=0
    while i<len(arr):
      if arr[i]==0:
        #start flip 
        start=i
        break
      else:
        i+=1
    while start<len(arr):
      arr[start]=1-arr[start]
      start+=1
  return count
