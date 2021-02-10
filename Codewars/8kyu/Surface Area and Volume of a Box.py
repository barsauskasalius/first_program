def get_size(w,h,d):
    volume = w * h * d
    area = 2 * d * w + 2 * d * h + 2 * w * h
    arr = [area, volume]
    return arr
    #https://www.codewars.com/kata/565f5825379664a26b00007c/train/python