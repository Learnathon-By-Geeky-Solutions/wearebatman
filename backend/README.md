## Documentation of the Backend
<br>

<p align="center">
    <img src="https://owpgcdswxgqcueyyzgur.supabase.co/storage/v1/object/public/statics/PMWw2YlT.jpeg" width="50%" />
</p>

<br>

### Setting up the repo

#### Setting up a python virtual environment
- Make sure python3-venv is in your machine
```bash
sudo apt install python3-venv
```
- Make a python virtual environment with the following command:
```bash
python3 -m venv .venv
```
- activate the environment
```bash
source .venv/bin/activate
```
- install the requirements
```bash
pip install -r requirements.txt
```

#### Running the Backend
Run the backend with the following command:
```bash
python manage.py runserver
```

#### Database Schema
[See the Database schema in Lucidchart](https://lucid.app/lucidchart/d5025ce3-6cdf-4695-8e99-55a7d24e5509/edit?viewport_loc=-11%2C-11%2C2219%2C1020%2C0_0&invitationId=inv_43b122f6-732b-4774-80ce-248f34f2222a)

#### Making changes and applying to the database
- Create Migration file
```bash
python manage.py makemigrations
```
- Apply the changes
```bash
python manage.py migrate
```
