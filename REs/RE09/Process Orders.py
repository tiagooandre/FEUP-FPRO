def invoice_totals(order, min):
    return list(map(lambda x: (x[0], x[2]*x[3]+10 if x[2]*x[3] < min else x[2]*x[3]), order))
print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95]], 0))