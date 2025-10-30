from django.core.management.base import BaseCommand
from training_app.models import User
import pandas as pd

class Command(BaseCommand):
    help = "Fetch users from MySQL using Django ORM, modify them, and export to CSV"

    def handle(self, *args, **kwargs):
        try:
            # Fetch all users from DB
            users = User.objects.all().values('id', 'first_name', 'last_name')

            # Convert to list of dicts
            user_list = list(users)

            if not user_list:
                self.stdout.write("No users found in the database.")
                return

            # Convert to DataFrame
            df = pd.DataFrame(user_list)

            # Insert new column at position 0
            df.insert(0, 'source', 'django')

            # Display the DataFrame
            self.stdout.write("\nFetched and modified data:\n")
            self.stdout.write(str(df))

            # Optional: Export to CSV
            # df.to_csv('user_data.csv', index=False)
            # self.stdout.write("\nData written to user_data.csv successfully.")

        except Exception as e:
            self.stderr.write(f"\nError: {e}")
