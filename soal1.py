def analisis_review_aplikasi(reviews):
    if not reviews:
        return None, None, None
    min_rating = min(reviews)
    max_rating = max(reviews)
    if (min_rating%1==0):
      min_rating = int(min(reviews))
    if (max_rating%1==0):
      max_rating = int(max(reviews))
    avg_rating = sum(reviews) / len(reviews)

    return min_rating, max_rating, avg_rating

input1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
input2 = [1, 5, 2.9, 5, 4, 2.5, 5, 3.6, 1.1, 3.6, 4, 4.2, 1.5]

min1, max1, avg1 = analisis_review_aplikasi(input1)
min2, max2, avg2 = analisis_review_aplikasi(input2)

print("[4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0] \t: [", min1, max1, avg1, "]")
print("[1, 5, 2.9, 5, 4, 2.5, 5, 3.6, 1.1, 3.6, 4, 4.2, 1.5] \t: [", min2, max2, avg2, "]")