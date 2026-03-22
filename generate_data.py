import pandas as pd
import random
import sqlite3
from faker import Faker

fake = Faker('en_IN')

# Configuration
NUM_USERS = 5000
NUM_PROVIDERS = 500
NUM_BOOKINGS = 5000

CATEGORIES = ['Plumbing', 'Electrical', 'Cleaning', 'Carpentry', 'Appliance Repair', 'Pest Control']
STATUSES = ['Completed', 'Completed', 'Completed', 'Cancelled by User', 'Cancelled by Provider', 'No Show']
CANCELLATION_REASONS_USER = ['Found a cheaper alternative', 'Issue resolved itself', 'Provider delayed', 'Changed my mind']
CANCELLATION_REASONS_PROVIDER = ['Emergency', 'Distance too far', 'Equipment breakdown', 'Overbooked']

# 1. Generate Users
print("Generating Users...")
users_data = []
for i in range(1, NUM_USERS + 1):
    users_data.append({
        'user_id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'city': fake.city(),
        'signup_date': fake.date_between(start_date='-2y', end_date='today')
    })
df_users = pd.DataFrame(users_data)

# 2. Generate Providers
print("Generating Providers...")
providers_data = []
for i in range(1, NUM_PROVIDERS + 1):
    providers_data.append({
        'provider_id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'service_category': random.choice(CATEGORIES),
        'rating': round(random.uniform(2.5, 5.0), 2),
        'city': fake.city(),
        'onboarding_date': fake.date_between(start_date='-2y', end_date='today')
    })
df_providers = pd.DataFrame(providers_data)

# 3. Generate Bookings
print("Generating Bookings...")
bookings_data = []
for i in range(1, NUM_BOOKINGS + 1):
    status = random.choice(STATUSES)
    
    cancel_reason = None
    if status == 'Cancelled by User':
        cancel_reason = random.choice(CANCELLATION_REASONS_USER)
    elif status == 'Cancelled by Provider':
        cancel_reason = random.choice(CANCELLATION_REASONS_PROVIDER)
        
    service_date = fake.date_between(start_date='-1y', end_date='today')

    bookings_data.append({
        'booking_id': i,
        'user_id': random.randint(1, NUM_USERS),
        'provider_id': random.randint(1, NUM_PROVIDERS),
        'service_date': service_date,
        'booking_status': status,
        'cancellation_reason': cancel_reason,
        'service_amount': round(random.uniform(200.0, 3000.0), 2)
    })
df_bookings = pd.DataFrame(bookings_data)

# 4. Create SQLite Database
print("Creating SQLite database...")
# This creates the database file in your project folder
conn = sqlite3.connect('localfix.db') 

# Write the dataframes directly to SQL tables
df_users.to_sql('Users', conn, if_exists='replace', index=False)
df_providers.to_sql('Providers', conn, if_exists='replace', index=False)
df_bookings.to_sql('Bookings', conn, if_exists='replace', index=False)

conn.close()
print("Database created successfully! Look for 'localfix.db' in your folder.")