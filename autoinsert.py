import util, cadnano

def insertExtraBp(part, settings):
    tbp = settings.get('targetBpbetweenInsertions')
    noi = settings.get('numOfInsertions')
    initOffset = settings.get('initialPosition')
    incr = 1
    if part != None:
        initPos = -1
        offset = initOffset 
        for vh in part.getVirtualHelices():
            scafSS = vh.scaffoldStrandSet()
            y = 0
            for strand in scafSS:
                lo, hi = strand.idxs()
                if strand.hasInsertion():
                    for ins in strand.insertionsOnStrand():
                        strand.removeInsertion(ins.idx())
                if initPos == -1:
                    initPos = lo + offset
                numOfBp = ((hi - lo) // tbp) + noi
                for x in range(0, numOfBp):
                    rangeOffset = initPos + (y * tbp)
                    if (rangeOffset <= hi):
                        strand.addInsertion(rangeOffset, noi)
                        y += 1
                    incr += 1
# end def


cadnano.app().insertExtraBp = insertExtraBp
