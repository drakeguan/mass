# How to start a Revolution ?

## Know your Goal
```
import mass
from mass import Revolution, Step, Action, at_the_same_time

revolution = Revolution()
with revolution.Plan('The Network Revolution'):
    with Step('Marketing'):
        Action('market research', by='sales', from='Taiwan')
    with at_the_same_time():
        with Step('Production Development'):
            Action('create mockup', by='artist', from='Taiwan')
            Action('build system', by='developer', from='Taiwan')
        with Step('Customer Development'):
            Action('create ads', by='sales', from='Taiwan')
    with Step('Hit the Market'):
        Action('release system', by='developer', from='Taiwan')
```

## Build your Support
```
from mass import Proles
proles = Proles('Taiwan')

@proles.role('developer')
def process_shell(action):
    print 'do develop work for', action

@proles.role('artist')
def process_shell(action):
    print 'do art work for', action

@proles.role('sales')
def process_shell(action):
    print 'do sales work for', action

if __name__ == "__main__":
    proles.wake()
```

## FIGHT!
```
mass.start(revolution)
```
