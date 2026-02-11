import json
import os
import pandas as pd


def extract_transaction_data():
    data_path = "pulse/data/aggregated/transaction/country/india/state/"
    data = []

    states = os.listdir(data_path)

    for state in states:
        state_path = os.path.join(data_path, state)

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)

            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        json_data = json.load(f)

                        for transaction in json_data["data"]["transactionData"]:
                            data.append({
                                "state": state.replace("-", " ").title(),
                                "year": int(year),
                                "quarter": int(file.replace(".json", "")),
                                "transaction_type": transaction["name"],
                                "transaction_count": transaction["paymentInstruments"][0]["count"],
                                "transaction_amount": transaction["paymentInstruments"][0]["amount"]
                            })

    df = pd.DataFrame(data)
    return df   




def extract_user_data():
    data_path = "pulse/data/aggregated/user/country/india/state/"
    data = []

    states = os.listdir(data_path)

    for state in states:
        state_path = os.path.join(data_path, state)

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)

            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        json_data = json.load(f)

                        data.append({
                            "state": state.replace("-", " ").title(),
                            "year": int(year),
                            "quarter": int(file.replace(".json", "")),
                            "registered_users": json_data["data"]["aggregated"]["registeredUsers"],
                            "app_opens": json_data["data"]["aggregated"]["appOpens"]
                        })

    df = pd.DataFrame(data)
    return df



def extract_insurance_data():
    data_path = "pulse/data/aggregated/insurance/country/india/state/"
    data = []

    states = os.listdir(data_path)

    for state in states:
        state_path = os.path.join(data_path, state)

        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)

            for file in os.listdir(year_path):
                if file.endswith(".json"):
                    file_path = os.path.join(year_path, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        json_data = json.load(f)

                        for item in json_data["data"]["transactionData"]:
                            data.append({
                                "state": state.replace("-", " ").title(),
                                "year": int(year),
                                "quarter": int(file.replace(".json", "")),
                                "insurance_count": item["paymentInstruments"][0]["count"],
                                "insurance_amount": item["paymentInstruments"][0]["amount"]
                            })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    transaction_df = extract_transaction_data()
    transaction_df.to_csv("transaction_data.csv", index=False)

    user_df = extract_user_data()
    user_df.to_csv("user_data.csv", index=False)

    insurance_df = extract_insurance_data()
    insurance_df.to_csv("insurance_data.csv", index=False)

    print("All aggregated data extracted successfully!")


