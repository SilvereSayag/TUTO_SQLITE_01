import sqlite3
from Song import Song
from Playlist import Playlist
import sql_test  as sql

def main() -> None:

    # conn = sqlite3.connect(":memory:")

    conn = sql.connect_to_dB()

    cursor = conn.cursor()

    sql.create_tables(conn, cursor)

    s_1 = Song("Africa", "Toto")
    s_2 = Song("Bob Morane", "Indochine")

    p_1 = Playlist("ma premiere playlist")

    print("\n")

    print(f"S1 : {s_1}")
    print(f"S2 : {s_2}")

    s_1.votes = 9

    print(f"S1 : {s_1}")

    print("\n")

    print(f"playlist : {p_1}")
    print(f"songs : {p_1.get_songs}")

    p_1.add_song(s_1)
    p_1.add_song(s_2)

    print("\n")
    print(f"playlist : {p_1}")
    print(f"songs : {p_1.get_songs}")

    print("\ninsert_song(s_1)")
    sql.insert_song(s_1, conn, cursor)
    sql.insert_song(s_2, conn, cursor)
    sql.print_songs(cursor)

    

    # print("\nprint(get_song_by_title(Africa))")
    # update_song_vote(s_1, 99, conn, cursor)
    # print(f"oustide fun : {get_song_by_title("Africa", cursor)}")
    # print_songs(cursor)

    # print("\nremove_song(s_1)")
    # remove_song(s_1, conn, cursor)
    # print_songs(cursor)

    # conn.commit()

    # conn.close()

    # cursor.execute("""INSERT INTO songs VALUES ('alpha', 'Cure', 0)""")
    # cursor.execute("""INSERT INTO songs VALUES ('Beta', 'Depeche Mode', 0)""")
    # cursor.execute("""INSERT INTO songs VALUES ('CCC', 'Male', 0)""")


if __name__ == "__main__":
    main()
