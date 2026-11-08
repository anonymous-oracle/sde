def layer_cost(utilisation_factors, rental_ratio):
    cost = 0
    should_own = rental_ratio > 1
    for utilisation_factor in utilisation_factors:
        if should_own:
            cost += min(8760*rental_ratio*utilisation_factor, 8760)
        else:
            cost += 8760*rental_ratio*utilisation_factor
    return cost

if __name__ == "__main__":
    utilisation_factor = [1.0, 0.6, 0.3, 0.1]
    print(layer_cost(utilisation_factor, 3))