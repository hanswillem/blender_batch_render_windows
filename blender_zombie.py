import sys
import subprocess


def main():
    print('starting script...')

    batch_file = 'batch_render.bat'

    while True:

        #pick first available file
        f = open(batch_file, 'r')
        picked_file = None
        for i in f:
            print()
            if not i[:2] == '//':
                picked_file = i
                break
        f.close()

        if picked_file == None:
            print('no more files to render')
            sys.exit()

        #add prefix to line
        f = open(batch_file, 'r')
        l = []
        for i in f:
            if i == picked_file:
                i = '//' + picked_file
            l.append(i)
        f.close()

        #save .bat file
        f = open(batch_file, 'w')
        for i in l:
            f.write(i)
        f.close()

        #start render
        subprocess.call(picked_file, shell = True)


if __name__ == '__main__':
    main()
