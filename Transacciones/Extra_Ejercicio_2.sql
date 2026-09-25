DO $$

DECLARE 
    V_Customer_ID VARCHAR(40) := 'U001';
    V_Bill_ID VARCHAR(40) := 'B007';
    V_Product_Record RECORD;
    V_Stock_Product INTEGER;



BEGIN

    INSERT INTO Bills (ID, USER_ID, Status)
        VALUES (V_Bill_ID, V_Customer_ID, 'Pending');

    INSERT INTO Bill_Details (ID, Bill_ID, Product_ID, Quantity, Unit_Price, Product_Status)
        VALUES ('D008', V_Bill_ID, 'P001', 10, 2, 'Pending'),
            ('D009', V_Bill_ID, 'P002', 15, 2.5, 'Pending'),
            ('D010', V_Bill_ID, 'P003', 25, 1, 'Pending'),
            ('D011', V_Bill_ID, 'P004', 22, 1, 'Pending'),
            ('D012', V_Bill_ID, 'P005', 34, 2.5, 'Pending');


        FOR V_Product_Record IN (
        SELECT Quantity, Product_ID
        FROM Bill_Details
        WHERE Bill_ID = V_Bill_ID
        )

        LOOP 

        SELECT Inventory INTO V_Stock_Product
        FROM Products
        WHERE ID = V_Product_Record.Product_ID;

        IF V_Product_Record.Quantity IS NULL OR V_Stock_Product < V_Product_Record.Quantity THEN
        RAISE EXCEPTION '-- Stock Not Available--'; 

        END IF;

        UPDATE Products
        SET Inventory = Inventory - V_Product_Record.Quantity
        WHERE ID = V_Product_Record.Product_ID;

        END LOOP;

    UPDATE Bills
    SET Status = 'Awaiting Shipment'
    WHERE ID = V_Bill_ID;


    RAISE NOTICE '--The order has been completed--';

END;

$$LANGUAGE plpgsql;

