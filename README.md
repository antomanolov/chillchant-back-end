# chillchant-back-end

# When the website is finished will have:
1.Login/logout system. <br/>
2.Message system. <br/>
3.Different modes (dark, light, different font selection etc.) <br/>
4.Fully responsive design. <br/>
5.DB(maybe PostgreSQL) <br/>
6.The option of doing every CRUD operation. <br/>

## 1. Login/Logout/Admin panel

The app is working with custom user model(AppUser), which is fully working. The authentication is made to be with email, not with username(this can be seen in the model.py).<br> 
The data is saved on DB. For dev I will use SQLite, but when in prod will be changed with PosgtresSQL.<br>
This is how the custom admin panel is looking.<br>
### Home
![image](https://github.com/antomanolov/chillchant-back-end/assets/95758427/7b001fe2-5e7b-4038-8211-7a1608683221)

### Add user(this can be further cusomized for the need of the admins. I choose to keep it like that for the sake of the pattern)
![image](https://github.com/antomanolov/chillchant-back-end/assets/95758427/12b8e15c-8f1c-4fe5-ba52-a08c0de044fe)

### Change user with filters
![image](https://github.com/antomanolov/chillchant-back-end/assets/95758427/4643d46e-282f-4abc-b8f1-0a84f090e220)

### Edit user, add perms, delete the user etc.
![image](https://github.com/antomanolov/chillchant-back-end/assets/95758427/31013ff3-899a-4276-8f29-15ba061c3b09)
![image](https://github.com/antomanolov/chillchant-back-end/assets/95758427/21d51f3f-bd2a-4f39-b647-6e9f8c13a6d4)

Everything is custom, to the need of the app.
