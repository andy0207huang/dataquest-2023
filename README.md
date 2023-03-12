# dataquest-2023
Hotel Cancellation Machine Learning Model

## Consideration:
1. not all the Canceled vs Non_Canceled are the same, weighted accuracy
2. 

## Feature Engineering:
1. ✅ [Arrival Month, Arrival Date] can be turned into "season categorical" by grouping
    - Season in Italy: 
        - Spring: March to May
        - Summer: June to August
        - Fall: September to Novemeber 
        - Winter: December to February
    - Get number of bookings, cancelled, non cancelled
2. Grouping the rows based on market segment
3. sum ( [AvgRoomPrice] * [BookingStatus = Canceled] ) = $$$ lost in cancelled reservation
4. Grouping rows based on room type
5. 

## Graphs Shown:
1. compare to [LeadTime, MarketSegment, RoomType] Canceled vs Not_Canceled
2. 

