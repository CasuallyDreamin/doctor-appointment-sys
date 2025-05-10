# doctor-appointment-sys
a platform to book and manage doctor appointments
# How to use:
run the main.py file with python
$ python3 main.py $

# Note:
    No duplicate data is made when adding data objects to data structures

    the only extra space used when adding to multiple
    data structrures is pointer space

    Given deletion is not a required operation, security concerns of hanging pointers are unfounded.

# data structures
## parent-child linked list:
    a main linked list of parent nodes
    
    each parent node contains a singly linked list (children)
    
    used to get doctors/patients by city/speciality
    
    parent node could also hold another data structure as children 
    visualization:
        
        p1 -> p2 -> p3 -> None
        |      |    |
        v      v    v
        c1     c1   c1
        |      |    |
        v      v    v
        c2     c2   None
        |      |    
        v      v
        None   None
    
## Hashtable
    used for getting doctors/patients by phone number/national id at O(1)

## singly linked list
    used to implement parent-child linked list
    also used to show data and check for existing data if hashtable was not available

## array
    used to implement hashtables

## phase 1
#### doctor registeration

### admin panel
#### See all doctors
#### Find doctor by national ID
#### Find all doctors by speciality
#### Add city support
#### Add speciality support  

## phase 2

### doctor's panel
#### login as doctor

### patient's panel
#### login as patient

# structural details
## main.py:
 main driver component

## doctors/patients.py:
 wrapper classes for data structures used to store doctor/patient objects

## UI.py:
contains all menu's as functions
calls main_menu, takes an option and calls the proper menu to render

also contains:
    view_model as vm: middle man between the ui and the data classes (doctors.py / patients.py)

    init(): reads data files and adds them to data classes

## folders
### data files:
    test data to check app functionality. also used to store data upon exit.
### data objects
    patient.py and doctor.py: holds data for a patient/doctor

### data structures
    contains data structure classes used to store data objects
