import time
import random
from PQ import PriorityQueue

t_promedio =[]

def test_insertion_extraction(num_elements, num_trials):
    # Show test header
    print
    print('------------------------------------')
    print('  TESTING INSERTION AND EXTRACTION  ')
    print('------------------------------------')
    print()

    # Run test num trials
    for trial in range(num_trials):
        # Generate random numbers
        a = [i for i in range(num_elements)] # (a) almacena los indices.
        random.shuffle(a)

        # Create priority queue
        pq = PriorityQueue()

        # init time
        #t0 = time.clock()  # medir tiempo

        # Insert elements in PQ
        for x in a:
            # Insert element and priority
            pq.insert_or_update(x, str(x)) # va insertando prioridades aleatorias.


        #final time
        #t1 = time.clock() - t0
        #t_promedio.append(t1)
        #print("Time elapsed: ", t1)  # CPU seconds elapsed (floating point)

        # Set failed flag
        failed_trial = False


        # init time
        # t0 = time.clock()  # medir tiempo

        # init time
        #t0 = time.clock()  # medir tiempo


        # Testing extraction (in order)
        for i in range(num_elements):
            # Get item
            item = pq.extract()
            priority = item[0] # guarda la prioridad
            data = item[1] # guarda la data

            # Check item
            if priority != i:  # Compara la prioridad con el valor esperado.
                # Set failed flag
                failed_trial = True

                # Print error
                print('   FAIL: Element #%d is %d' % (i, priority))

                # Break trial
                break

        #final time
        #t1 = time.clock() - t0
        #t_promedio.append(t1)
        #print("Time elapsed: ", t1)  # CPU seconds elapsed (floating point)

        # Print test result
        if failed_trial:
            # Print failed trial
            print('Trial #%2d: FAIL' % (trial + 1))
        else:
             # Print success trial
            print('Trial #%2d: OK' % (trial + 1))



def test_insertion_update_extraction(num_elements, num_trials):
    # Show test header
    print()
    print('--------------------------------------------')
    print('  TESTING INSERTION, UPDATE AND EXTRACTION  ')
    print('--------------------------------------------')
    print()

    # Run test num trials
    for trial in range(num_trials):
        # Generate random numbers
        a = [i for i in range(num_elements)]
        random.shuffle(a)

        # Create priority queue
        pq = PriorityQueue()



        # Insert elements in PQ
        for x in a:
            # Insert element and priority
            pq.insert_or_update(3 * x, str(x))

        #print pq

        # Generate random numbers
        a = [i for i in range(num_elements)]
        random.shuffle(a)


        # init time
        t0 = time.clock()  # medir tiempo

        # Update elements
        for x in a:
            # Insert element and priority
            pq.insert_or_update(x, str(x))

        #print pq
        #final time
        t1 = time.clock() - t0
        t_promedio.append(t1)
        print("Time elapsed: ", t1)  # CPU seconds elapsed (floating point)


        # Set failed flag
        failed_trial = False

        #init time
        #t0 = time.clock() #medir tiempo

        # Testing extraction (in order)
        for i in range(num_elements):
            # Get item
            item = pq.extract()
            priority = item[0]
            data = item[1]

            # Check item
            if priority != i:
                # Set failed flag
                failed_trial = True

                # Print error
                print('   FAIL: Element #%d is %d' % (i, priority))

                # Break trial
                break

        #t1 = time.clock() - t0
        #print("Time elapsed: ", t1)  # CPU seconds elapsed (floating point)

        # Print test result
        if failed_trial:
            # Print failed trial
            print ('Trial #%2d: FAIL' % (trial + 1))
        else:
             # Print success trial
            print ('Trial #%2d: OK' % (trial + 1))



if __name__ == '__main__':

    n= 10000
    # Test insertion & extraction
    test_insertion_extraction(n, 15)


    # Test insertion, update & extraction
    test_insertion_update_extraction(n, 15)

    '''
    promedio =0
    for i in range(len(t_promedio)):
        promedio = promedio + t_promedio[i]


    print(f"Tiempo promedio con {n} elementos: {promedio/len(t_promedio)} seg")
    '''