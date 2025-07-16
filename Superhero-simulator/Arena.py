  # Hero1 attacks hero2
    hero1_attack = hero1.sum_of_attacks()
    print(f"{hero1.name} attacks with a total damage of {hero1_attack}")

    # Hero2 defends
    hero2_defense = hero2.defend()
    print(f"{hero2.name} defends with a total block of {hero2_defense}")

    # Print the final battle result
    final_damage = hero1_attack - hero2_defense
    hero2.current_health -= max(final_damage, 0)
    print(f"{hero2.name}'s Health after attack: {hero2.current_health}")

    # Determine the winner
    if hero2.current_health <= 0:
        print(f"{hero1.name} wins the battle!")
    else:
        print(f"{hero2.name} is still standing!")

    # Battle between two heroes (randomized winner)
    hero1.battle(hero2)

if __name__ == "__main__":
    main()
