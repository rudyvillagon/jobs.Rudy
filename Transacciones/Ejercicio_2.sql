Do $$

DECLARE 
    V_Stock_Available INTEGER;
    V_User_On_DB VARCHAR(40);

BEGIN

    SELECT Inventory INTO V_Stock_Available
    FROM Products
    WHERE ID = 'P003';

    SELECT Name INTO V_User_On_DB
    FROM Users
    WHERE ID = 'U005';

    If V_Stock_Available IS NULL OR V_Stock_Available < 2 THEN
    RAISE EXCEPTION '--Stock Not Available--';
    END IF;

    If V_User_On_DB IS NULL THEN
    RAISE EXCEPTION '--USER DOES NOT EXIST--';
    END IF;

    INSERT INTO Bills (ID, User_ID)
        VALUES ('B006', 'U005');

    INSERT INTO Bill_Details (ID, Bill_ID, Product_ID, Quantity, Unit_Price)
        VALUES ('D006', 'B006', 'P003', 2, 1);


    UPDATE Products
    SET Inventory = Inventory - 2
    WHERE ID = 'P003';

    RAISE NOTICE 'Transaction Complete';

END;

$$ LANGUAGE plpgsql;