price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print(price)

rating = 4
 
ratings = print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')


from datetime import datetime

dt = datetime.now()
today = dt.strftime('%A').lower()

whatToDo = print('pomagam mamie') if today == 'monday' else print('ty masz w domu pranie') if today == 'tuesday' else print('ty masz w domu pranie') if today == 'wednesday' else print('ja mam dyżur') if today == 'thursday' else print('ja mam dwa zebraniea') if today == 'friday' else print('ty na lekcje ganiasz') if today == 'saturday' else print('to czas dla nas') 