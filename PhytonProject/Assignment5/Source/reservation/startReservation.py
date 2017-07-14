from Assignment5.Source.reservation.AirlineReservation import AirlineReservation
from Assignment5.Source.reservation.HotelReservation import HotelReservation

A1 = AirlineReservation("1","Vinuthna","Gummadi","Business Class","07-13-2017")
A1.CheckAvailability()
A1.currentStatus("Airline")
H1 = HotelReservation("1","Vinuthna","Gummadi","Penthouse","07-07-2014","07-13-2017")
H1.CheckAvailability()
H1.currentStatus("Hotel")
