from Assignment5.Source.reservation.Airline import Airline
from Assignment5.Source.reservation.Customer import Customer
from Assignment5.Source.reservation.Reservation import Reservation


class AirlineReservation(Reservation):

    airline=None
    def __init__(self,passenger_id,passenger_fname,passenger_lname,airline_seat_section,
         airline_departure_date):

       customer = Customer(passenger_id,passenger_fname,passenger_lname)
       AirlineReservation.airline = Airline(airline_seat_section,airline_departure_date)
       super(AirlineReservation, self).__init__(customer,AirlineReservation.airline)
       self.airline_seat_section =airline_seat_section
       self.airline_departure_date = airline_departure_date

    def CheckAvailability(self):
        if  (AirlineReservation.airline.airline_seats.get(self.airline_seat_section) != 0):
            AirlineReservation.airline.airline_seats[self.airline_seat_section] -= 1
            self.passenger_record['p_wallet'] +=        AirlineReservation.airline.airline_price[self.airline_seat_section]
            print ("\n\nReserved Airline Ticket\n\n")