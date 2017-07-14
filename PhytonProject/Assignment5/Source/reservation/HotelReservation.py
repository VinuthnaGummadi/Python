from Assignment5.Source.reservation.Customer import Customer
from Assignment5.Source.reservation.Hotel import Hotel
from Assignment5.Source.reservation.Reservation import Reservation


class HotelReservation(Reservation):
    hotel = None
    def __init__(self,passenger_id,passenger_fname,passenger_lname,hotel_room_selection,
             hotel_check_in_date,hotel_check_out_date):
        customer = Customer(passenger_id, passenger_fname, passenger_lname)
        HotelReservation.hotel = Hotel(hotel_room_selection,hotel_check_in_date)
        super(HotelReservation, self).__init__(customer,HotelReservation.hotel)
        self.hotel_room_selection = hotel_room_selection
        self.hotel_check_in_date = hotel_check_in_date
        self.hotel_check_out_date = hotel_check_out_date

    def CheckAvailability(self):
        if ( HotelReservation.hotel.hotel_room.get(self.hotel_room_selection) != 0):
            HotelReservation.hotel.hotel_room[self.hotel_room_selection] -= 1
            self.passenger_record['p_wallet'] +=  HotelReservation.hotel.hotel_price[self.hotel_room_selection]
            print ("\n\nReserved Hotel Room\n\n")