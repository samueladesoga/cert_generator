import pandas as pd
from utils import create_certificate_for
from send_email import send_certificate

def generate_and_send_certificate_from_excel():
    # File path - replace with your actual Excel file path
    file_path = "Test Participant.xlsx"
    
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Check if the required columns exist
        if 'First name' not in df.columns or 'Last name' not in df.columns or 'Email' not in df.columns:
            print("Error: Excel file must contain 'First name', 'Last name', and 'Email' columns.")
            return
        
        # Concatenate first and last names with a space in between
        df['Full Name'] = df['First name'] + ' ' + df['Last name']
        
        # Print full name and email for each row
        for index, row in df.iterrows():
            print(f"Full Name: {row['Full Name']}, Email: {row['Email']}")
            print(create_certificate_for(row['Full Name']))
            send_certificate(row['Full Name'], row['Email'])
        
        print(f"\nTotal records processed: {len(df)}")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")