import freecurrencyapi
client = freecurrencyapi.Client('YOUR_API_KEY')


choice = input('Hello, press 1 for USD to CAD, and 2 for USD to AUD?')
if choice == '1':
       data = client.latest()
       usd_to_cad_rate = data['data']['CAD']


       your_amount_in_usd = int(input('What is your amount in US Dollars?'))
       your_amount_in_cad = your_amount_in_usd * usd_to_cad_rate


       print(your_amount_in_cad)


elif choice == '2':
       data = client.latest()
       usd_to_aud_rate = data['data']['AUD']


       your_amount_in_usd = int(input('What is your amount in US Dollars?'))
       your_amount_in_aud = your_amount_in_usd * usd_to_aud_rate


       print(your_amount_in_aud)


else:
   print('Invalid Choice, Have a great day!')
