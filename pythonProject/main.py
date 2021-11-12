



def SelectionSort() :
  List = [9, 3, 5, 3, 4, 6, 0]
  for i from 0 to List.Length:
    SmallestElement = List[i]
    for j from i to List.Length:
      if SmallestElement > List[j]:
        SmallestElement = List[j]
    Swap(List[i], SmallestElement)


