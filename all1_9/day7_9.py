def converter (usd_val) :
    inr_val = usd_val * 95.38
    return inr_val
usd = float(input("Enter the amount in USD: "))
inr = converter(usd)
print(f"{usd} USD is equal to {inr} INR.")
