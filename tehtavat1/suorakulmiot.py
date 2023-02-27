def area(rec1, rec2, rec3):
    # Difine max values for top left and bottom right coordinates
    # Top left
    top_left_x = min(rec1[0], rec2[0], rec3[0])
    top_left_y = max(rec1[1], rec2[1], rec3[1])
    top_left = (top_left_x, top_left_y)


    # Bottom right
    bottom_right_x = max(rec1[2], rec2[2], rec3[2])
    bottom_right_y = min(rec1[3], rec2[3], rec3[3])

    xpoints = (rec1[0], rec2[0], rec3[0])
    
    # TODO

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3))