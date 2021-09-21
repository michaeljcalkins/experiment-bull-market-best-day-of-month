import csv
import locale
locale.setlocale( locale.LC_ALL, '' )

print("===========================================")
print("= GROWTH STOCKS: OPTIMIZED MONTHLY BUYING =")
print("===========================================")

# TODO convert sell price and ticker to cli args 
# TODO tell me best day of month

sell_price = 21.50
ticker_filename = "t.csv"

with open("output.csv", "w") as output_file:
  output_writer = csv.writer(output_file)
  output_writer.writerow(["DAY", "SHARES", "PROFIT", "COST"])

  for day in range(1, 32):
    with open(ticker_filename) as read_file:
      next(read_file)
      reader = csv.reader(read_file)

      share_count = 0;
      cost_basis = 0;

      for row in reader:
        day_of_month = int(row[0].split("/")[1])
        close_price = locale.atof(row[1].strip("$"))

        if day_of_month == day:
          cost_basis += close_price
          share_count += 1
      
      net_liq = sell_price * share_count
      profit = net_liq - cost_basis
      output_writer.writerow([day, share_count, profit, cost_basis])

      print("DAY: {}, SHARES: {}, PROFIT: {}, COST: {}".format(day, share_count, locale.currency(profit), locale.currency(cost_basis)))