DO $$

DECLARE
    V_Bill_ID VARCHAR(40) := 'D003';
    V_Product_return INTEGER;

BEGIN    
    SELECT Quantity INTO V_Products_return
    FROM Bill_Details
    WHERE Bill_ID = V_Bill_ID;


    IF NOT EXISTS (
    SELECT *
    FROM Bill_Details 
    WHERE ID = V_Bill_ID
    ) THEN 

    RAISE EXCEPTION 'THE BILL DONT EXISTS'