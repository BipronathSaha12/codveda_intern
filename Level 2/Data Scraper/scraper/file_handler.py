# handle csv to json conversion
import csv 
import json
import os

class FileHandler:

    @staticmethod
    # Save data to CSV file
    def save_to_csv(data, filename="scraped_data.csv"):
        if not data:
            print("No data to save.")
            return

        keys = data[0].keys()
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data saved to {filename}")


    @staticmethod
    # Save data to JSON file
    def save_to_json(data, filename="scraped_data.json"):
        if not data:
            print("No data to save.")
            return

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f" Data saved to {filename}")