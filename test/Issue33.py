import Framework

class Issue33( Framework.TestCase ): # https://github.com/jacquev6/PyGithub/issues/33
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.repo = self.g.get_user( "openframeworks" ).get_repo( "openFrameworks" )

    def testOpenIssues( self ):
        self.assertEqual( len( list( self.repo.get_issues() ) ), 338 )

    ### @todo testClosedIssues when Repository.get_issues uses its 'state' parameter
