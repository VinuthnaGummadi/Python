class Reservation:
   def __init__(self,customer,airline):
      self.customer = customer

      self.cost = 0
      self.reservation_id = []
      self.passenger_record = {'p_name'  : customer.passenger_fname + customer.passenger_lname,
                             'p_id'    : customer.passenger_id,
                             'p_wallet': customer.cost,
                             'p_reservation_id': customer.reservation_id,
                            }
      self.airline = airline

   def __init__(self, customer, hotel):
       self.customer = customer

       self.cost = 0
       self.reservation_id = []
       self.passenger_record = {'p_name': customer.passenger_fname + customer.passenger_lname,
                                'p_id': customer.passenger_id,
                                'p_wallet': self.cost,
                                'p_reservation_id': self.reservation_id,
                                }
       self.hotel = hotel

   def currentStatus(self,option):
       if option == "Airline":
           for key, value in self.airline.airline_seats.items():
              print (key, value)
       elif option == "Hotel":
           for key,value in self.hotel.hotel_room.items():
              print (key, value)

   def Total(self):
       print (self.passenger_record['p_wallet'])