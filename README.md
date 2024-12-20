Use git pull or clone or create file by hand, etc:

┌─[zerokool@skynet]─[/srv/salt]
└──╼ $ sudo git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 2), reused 0 (delta 0)
Unpacking objects: 100% (4/4), done.
From github.com:knightmare/saltstack
   1005fea..60ace18  master -> origin/master
Updating 1005fea..60ace18
Fast-forward
 _modules/screenprint.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

## then on the minions, you would want to sync it

┌─[zerokool@skynet]─[/srv/salt]
└──╼ $ sudo salt 'windows-test-minion' saltutil.sync_modules
windows-test-minion:
    - modules.screenprint
```

This indicates the module is now copied over, so let's test:

NB: This needs run on every minion, but this is a good way to test the water.

```
┌─[zerokool@skynet]─[/home/knightmare]
└──╼ $ sudo salt 'windows-test-minion' screenprint.screen_print "This is a test message" color=green
windows-test-minion:
    This is a test message
```

To use this inside a salt state file, in this case as part of the bucketman.enumerate.sls file:

```
## Logic for Windows minon
{% if grains['beverage'] != 'Irn Bru' %}
print_custom_message_no_irn_bru:
  module.run:
    - name: screenprint.screen_print
    - message: "Beverage is not Irn Bru, presuming it will be Faxe Kondi..."
    - color: "cyan"
```

Which renders like this:

```
┌─[zerokool@skynet]─[/srv/salt]
└──╼ $ sudo salt 'windows-test-minion' state.apply bucketman.enumerate
windows-test-minion:
:< snip>
----------
          ID: print_custom_message_no_irn_bru
    Function: module.run
        Name: screenprint.screen_print
      Result: True
     Comment: Module function screenprint.screen_print executed
     Started: 17:12:58.966471
    Duration: 1.089 ms
     Changes:
              ----------
              ret:
                  Beverage is not Irn Bru, presuming it will be Faxe Kondi...
: <snip>
Summary for windows-test-minion
------------
Succeeded: 1 (changed=1)
Failed:    0
------------
Total states run:     5
Total run time:   7.078 ms
```

I am fairly sure there is a better, faster, stronger way to do this, but I could not see anything in the saltstack documentation beyond the `test.nop` function, which did not render correctly, or give the correct output in a for loop.
