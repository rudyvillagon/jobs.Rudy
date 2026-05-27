Do $$

DECLARE 
    V_Stock_Product_1 INTEGER;
    V_Stock_Product_2 INTEGER;
    V_Product_Order_Quantity_1 INTEGER := 2;
    V_Product_Order_Quantity_2 INTEGER := 3;
    V_User_On_DB VARCHAR(40);

BEGIN

    SELECT Inventory INTO V_Stock_Product_1
    FROM Products
    WHERE ID = 'P003'; --Product 1

    SELECT Quantuty INTO V_Stock_Product_2
    FROM Products
    WHERE ID = 'P001'; --Product 2

    SELECT Name INTO V_User_On_DB
    FROM Users
    WHERE ID = 'U005';

    If V_Stock_Product_1 IS NULL OR V_Stock_Product_1 < V_Stock_Product_1 THEN
    RAISE EXCEPTION '-- P003 Stock Not Available--'; --Product 1
    END IF;

    If V_Stock_Product_2 IS NULL OR V_Stock_Product_2 < V_Stock_Product_2 THEN
    RAISE EXCEPTION '-- P001 Stock Not Available--'; --Product 2
    END IF;

    If V_User_On_DB IS NULL THEN
    RAISE EXCEPTION '--USER DOES NOT EXIST--';
    END IF;

    INSERT INTO Bills (ID, User_ID)
        VALUES ('B006', 'U005');

    INSERT INTO Bill_Details (ID, Bill_ID, Product_ID, Quantity, Unit_Price)
        VALUES ('D007', 'B006', 'P003', 2, 1); --Product 1

    INSERT INTO Bill_Details (ID, Bill_ID, Product_ID, Quantity, Unit_Price)
        VALUES ('D006', 'B006', 'P001', 3, 2); --Product 2

    UPDATE Products
    SET Inventory = Inventory - 2
    WHERE ID = 'P003'; --Product 1

    UPDATE Products
    SET Inventory = Inventory - 3
    WHERE ID = 'P001'; --Product 2

    RAISE NOTICE 'Transaction Complete';

END;

$$ LANGUAGE plpgsql;