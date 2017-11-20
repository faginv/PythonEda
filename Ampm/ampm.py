# Convert AM and PM Hour
# -->> I'm not sure whtat he is going to do.


new_lead_time_schedule = datetime.strptime(sale_order_line.order_id.date_order, DEFAULT_SERVER_DATETIME_FORMAT) + datetime.timedelta(days=sale_order_line.customer_lead or 0.0)

    if sale_order_line.shift2 == 'morning':
        new_lead_time_schedule = fields.Datetime.context_timestamp(self, timestamp = new_lead_time_schedule).replace(hour=0, minute=0, second=0).astimezone(utc)

    elif sale_order_line.shift2 == 'afternoon':
        new_lead_time_schedule = fields.Datetime.context_timestamp(self, timestamp = new_lead_time_schedule).replace(hour=4, minute=0, second=0).astimezone(utc)
